import { readdir } from "node:fs/promises";
import { writeFile } from "node:fs/promises";
import path from "node:path";

const PAGES_DIR = path.resolve("pages");
const OUTPUT_FILE = path.resolve("pages-index.json");

async function walk(dir, relBase = "") {
  const entries = await readdir(dir, { withFileTypes: true });
  let files = [];

  for (const entry of entries) {
    const relPath = relBase ? `${relBase}/${entry.name}` : entry.name;

    if (entry.isDirectory()) {
      files = files.concat(await walk(path.join(dir, entry.name), relPath));
    } else if (entry.isFile() && /\.md$/i.test(entry.name)) {
      files.push(relPath.split(path.sep).join("/"));
    }
  }

  return files;
}

const files = await walk(PAGES_DIR);
await writeFile(OUTPUT_FILE, JSON.stringify(files.sort(), null, 2));
console.log(`pages-index.json: ${files.length} файлов`);
