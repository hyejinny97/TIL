## ▶ 서버사이드 렌더링 함수 사용해보기 - `renderToNodeStream`

- `renderToString` 함수: 모든 렌더링 과정이 끝나야 문자열로 된 결과값을 반환함
- `renderToNodeStream` 함수: 호출 즉시 노드의 스트림(stream) 객체를 반환함

#### ➕ 참고) 노드의 스트림

- 스트림은 배열이나 문자열 같은 데이터 컬렉션임
- 크기가 큰 데이터를 다룰 때 유용함
- 스트림은 **데이터를 청크 단위로 쪼개서 전달**하기 때문에, 데이터가 완전히 준비되지 않아도 전송을 시작할 수 있음

- 일반적인 파일 읽기 코드

  - 단점) 크기가 큰 파일을 읽는 경우, 파일 전체 내용을 메모리로 가져오기 때문에 메모리에 여유가 없다면 부담이 될 수 있음

  ```js
  app.get("/readFile", (req, res) => {
    fs.readFile("./big_file.zip", (err, data) => {
      if (err) throw err;
      res.end(data);
    });
  });
  ```

- 스트림을 이용한 파일 읽기 코드

  - 장점) 스트림을 사용하면 큰 파일을 읽을 때 **메모리를 효율적으로 사용**할 수 있을 뿐만 아니라, 첫 번째 청크가 준비되면 바로 전송을 시작하기 때문에 **데이터를 빠르게 전송**할 수 있음
  - `createReadStream` 함수: '읽기' 가능한 스트림(readable stream) 객체를 생성
  - 노드의 HTTP response 객체: '쓰기' 가능한 스트림(writable stream) 객체
  - 아래에선 읽기 가능한 스트림에 쓰기 가능한 스트림을 연결했음
  - **데이터는 읽기 가능한 스트림에서 쓰기 가능한 스트림 쪽으로 흐름**

  ```js
  app.get("readFile", (req, res) => {
    const fileStream = fs.createReadStream("./big_file.zip");
    fileStream.pipe(res);
  });
  ```

- '읽기'와 '쓰기'가 모두 가능한 스트림(duplex stream) 객체도 있음

  - 3개 이상의 스트림을 연결할 때 사용됨
  - 아래에서 transformStream1, transformStream2가 읽기와 쓰기가 가능한 스트림임
  - 아래에서 데이터 흐름

    - `readableStream` → `transformStream1` → `transformStream2` → `writableStream`

  - 읽기와 쓰기가 모두 가능한 스트림은 읽기 가능한 스트림이 생성한 데이터를 기반으로 추가적인 작업을 할 수 있음

  ```js
  readableStream
    .pipe(transformStream1)
    .pipe(transformStream2)
    .pipe(writableStream);
  ```

### 🔹 `renderToNodeStream` 함수 사용하기

- `renderToNodeStream` 함수를 사용하면 렌더링 데이터를 빠르게 전달할 수 있음

  - ∵ 첫 번째 청크가 준비되면 바로 전송을 시작하기 때문

- `renderToNodeStream` 함수는 '읽기' 가능한 스크림 객체를 생성함

- `renderToNodeStream` 함수를 이용하도록 'server.js' 파일을 수정하자

  - root 요소를 기준으로 이전/이후 문자열을 나눈 후, 이전 문자열을 바로 전송함
  - `write` 메서드는 여러 번 호출할 수 있음
  - `end` 메서드를 호출해야 전송이 종료됨
  - 스트림 방식에서는 더 이상 '\_\_STYLE_FROM_SERVER\_\_' 문자열을 사용하지 않기 때문에 지움
  - 대신, `styled-components`의 `interleaveWithNodeStream` 메서드를 호출해 `renderStream`에서 스타일 코드가 생성되도록 함
  - 따라서, '\_\_STYLE_FROM_SERVER\_\_' 문자열이 아닌 root 요소 내부에 스타일 코드가 삽입됨
  - '읽기' 가능한 스트림인 `renderStream`과 '쓰기' 가능한 스트림인 `res`를 연결함
  - `{ end: false }` 옵션은 스트림이 종료됐을 때 `res.end` 메서드가 자동으로 호출되지 않도록 함
  - 스트림이 종료되면 마지막으로 postfix 데이터를 전송하게 됨

  ```js
  // src/server.js
  // ...
  import { renderToNodeStream } from "react-dom/server";

  // ...
  const html = fs
    .readFileSync(path.resolve(__dirname, "../dist/index.html"), "utf8")
    .replace("__STYLE_FROM_SERVER__", "");

  // ...
  app.get("*", (req, res) => {
    // ...
    const isPrerender = prerenderPages.include(page);

    const result = (isPrerender ? prerenderHtml[page] : html).replace(
      "__DATA_FROM_SERVER__",
      JSON.stringify(initialData)
    );

    if (isPrerender) {
      ssrCache.set(cacheKey, result);
      res.send(result);
    } else {
      const ROOT_TEXT = '<div id="root"></div>';
      const prefix = result.substr(
        0,
        result.indexOf(ROOT_TEXT) + ROOT_TEXT.length
      );
      const postfix = result.substr(prefix.length);

      res.write(prefix);

      const sheet = new ServerStyleSheet();
      const reactElement = sheet.collectStyles(<App page={page} />);
      const renderStream = sheet.interleaveWithNodeStream(
        renderToNodeStream(reactElement)
      );

      renderStream.pipe(res, { end: false });
      renderStream.on("end", () => {
        res.end(postfix);
      });
    }
  });

  app.listen(3000);
  ```

### 🔹 스트림 방식에서 캐싱 구현하기

- 스트림 방식에서 캐싱을 구현하기 위해서는 스트림으로 전송되는 청크 데이터에 접근할 수 있어야 함

  - 따라서, '읽기' 가능한 스트림인 `renderStream`과 '쓰기' 가능한 스트림인 `res` 사이에 직접 구현한 스트림을 끼워 넣어야 함

- 스트림으로 렌더링한 결과를 캐싱하도록 'server.js' 파일을 수정하자

  - `transform` 함수: 청크 데이터를 받으면 호출되는 함수
  - `flush` 함수: 청크 데이터가 모두 전달된 후 호출되는 함수

    - 하나의 완성된 HTML 데이터를 만들고 캐싱함

  - '읽기'와 '쓰기'가 가능한 스트림 객체인 `Transform`을 두 스트림 사이에 연결함
  - 아래에서의 데이터 흐름

    - `renderStream` → `cacheStream` → `res`

  ```js
  // src/server.js
  // ...
  import { Transform } from "stream";

  function createCacheStream(cacheKey, prefix, postfix) {
    const chunks = [];
    return new Transform({
      transform(data, _, callback) {
        chunks.push(data);
        callback(null, data);
      },
      flush(callback) {
        const data = [prefix, Buffer.concat(chunks), postfix];
        ssrCache.set(cacheKey, data.join(""));
        callback();
      },
    });
  }

  // ...
  app.get("*", (req, res) => {
    // ...
    const cacheStream = createCacheStream(cacheKey, prefix, postfix);
    cacheStream.pipe(res);
    renderStream.pipe(cacheStream, { end: false });
    // ...
  });

  app.listen(3000);
  ```
