import fs from 'node:fs';
const records=JSON.parse(fs.readFileSync(new URL('../data/records.json',import.meta.url)));
const weather=JSON.parse(fs.readFileSync(new URL('../data/weather.json',import.meta.url)));
fs.writeFileSync(new URL('../bundle.js',import.meta.url),'const ARCHIVE = '+JSON.stringify({records,weather}).replace(/</g,'\\u003c')+';\n');
