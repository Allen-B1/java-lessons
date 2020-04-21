const hljs = require('highlightjs');
const md = require('markdown-it')({
	breaks: true,
	linkify: true,
}).use(require('markdown-it-mermaid').default)
	.use(require('markdown-it-sup'));

const fs = require('fs');
const TEMPLATE = fs.readFileSync("template.html", {encoding:"utf8"});
var files = fs.readdirSync(".");
for (let file of files) {
	if (file.endsWith(".md")) {
		let content = fs.readFileSync(file, {encoding:"utf8"});
		let rendered = md.render(content);
		rendered = TEMPLATE.replace(/\[TITLE\]/g, file.slice(0,-3)).replace(/\[CONTENT\]/g, rendered);
		fs.writeFileSync("html/" + file.slice(0,-3) + ".html", rendered);
	}
}
