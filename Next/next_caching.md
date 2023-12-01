## ▶ 서버사이드 렌더링 캐싱하기

- 넥스트에서 서버사이드 렌더링을 캐싱하기 위해 'server.js' 파일을 수정해보자

  - 서버사이드 렌더링 결과를 캐싱하기 위해 `lru-cache` 패키지를 이용함

  ```js
  // server.js
  // ...
  const url = require("url");
  const lruCache = require("lru-cache");

  const ssrCache = new lrcCache({
    max: 100,
    maxAge: 1000 * 60,
  });
  // ...

  app.prepare().then(() => {
    // id를 처리하는 코드...
    server.get(/^\/page[1-9]/, (req, res) => {
      return renderAndCache(req, res);
    });
    // *를 처리하는 코드...
  });

  async function renderAndCache(req, res) {
    const parsedUrl = url.parse(req.url, true);
    const cacheKey = parseUrl.path;

    if (ssrCache.had(cacheKey)) {
      res.send(ssrCache.get(cacheKey));
      return;
    }

    try {
      const { query, pathname } = parsedUrl;
      const html = await app.renderToHtml(req, res, pathname, query);

      if (res.statusCode === 200) {
        ssrCache.set(cacheKey, html);
      }

      res.send(html);
    } catch (err) {
      app.renderError(err, req, res, pathname, query);
    }
  }
  ```
