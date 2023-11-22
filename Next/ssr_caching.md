## ▶ 서버사이드 렌더링 캐싱하기

- 데이터가 자주 변하지 않는 페이지인 경우, 서버사이드 렌더링 결과를 캐싱해서 활용할 수 있음

- 우선, 캐싱을 위해 `lcu-cache` 패키지를 설치하자

  - 제한된 메모리 안에 캐싱 데이터를 저장하려면 지울 데이터를 결정하는 알고리즘이 필요함
  - `lru-cache` 패키지는 정해진 최대 캐시 개수를 초과하면 LRU(Least Recently Used) 알고리즘에 따라 가장 오랫동안 사용되지 않은 캐시를 제거함

  ```bash
  $ npm install lru-cache
  ```

- 서버사이드 렌더링 캐싱을 위해 'server.js' 파일을 수정하자

  - 최대 100개의 페이지를 캐싱하고, 각 아이템은 60초동안 캐싱되도록 설정함
  - `cacheKey`는 쿼리 파라미터를 포함하는 url임

  ```js
  // src/server.js
  // ...
  import lruCache from "lru-cache";

  // ...
  const ssrCache = new lruCache({
    max: 100,
    maxAge: 1000 * 60,
  });

  // ...
  app.get("*", (req, res) => {
    const parseUrl = url.parse(req.url, true);
    const cacheKey = parseUrl.path;

    if (ssrCache.has(cacheKey)) {
      res.send(ssrCache.get(cashKey));
      return;
    }

    // ...
    ssrCache.set(cacheKey, result);
    res.send(result);
  });

  app.listen(3000);
  ```
