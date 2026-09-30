const path = require("path");
const fs = require("fs");

const BASE = path.join(__dirname, "public");

function cleanUrls(req, res, next) {
  // Redireciona trailing slash para sem barra (exceto raiz)
  if (req.url !== "/" && req.url.endsWith("/")) {
    res.writeHead(301, { Location: req.url.slice(0, -1) });
    res.end();
    return;
  }

  // Clean URLs: se não tem extensão, tenta resolver com .html
  const urlPath = req.url.split("?")[0];
  if (urlPath !== "/" && !path.extname(urlPath)) {
    const htmlFile = path.join(BASE, urlPath + ".html");
    if (fs.existsSync(htmlFile)) {
      req.url = urlPath + ".html";
    }
  }

  next();
}

module.exports = {
  server: {
    baseDir: "public",
    middleware: [cleanUrls]
  },
  files: ["public/**/*"]
};
