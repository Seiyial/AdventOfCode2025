#!/usr/bin/env bun

const args = process.argv.slice(2);

if (args.length !== 3 && args.length !== 4) {
	console.log("Usage: bun day.ts <day> <part> <input> [debug]");
	console.log("  day: 1-12");
	console.log("  part: 1 or 2");
	console.log("  input: i or ii");
	console.log("  debug: (optional) p or d or debug");
	process.exit(1);
}

const day = parseInt(args[0]!);
if (isNaN(day) || day < 1 || day > 12) {
	console.log("Error: Day must be between 1 and 12");
	process.exit(1);
}

const part = parseInt(args[1]!);
if (isNaN(part) || (part !== 1 && part !== 2)) {
	console.log("Error: Part must be 1 or 2");
	process.exit(1);
}

const inputType = args[2];
if (inputType !== 'i' && inputType !== 'ii') {
	console.log("Error: Input must be 'i' or 'ii'");
	process.exit(1);
}

const shouldDebug = args.length === 4 && ['d', 'p', 'debug', 'print'].includes(args[3]!);
if (shouldDebug) {
	process.env.AOC_DEBUG = "on";
}

console.log(`\nDay ${day} | Qn ${part} | Input ${inputType.toUpperCase()}`);

const dayStr = day.toString().padStart(2, '0');
const inputFilePath = `day${dayStr}/__input-${inputType}.txt`;

let inputData: string;
try {
	const file = Bun.file(inputFilePath);
	inputData = await file.text();
	inputData = inputData.trim();
	if (!inputData) {
		console.log(`Error: Input file ${inputFilePath} is empty or missing.`);
		process.exit(1);
	}
} catch (e) {
	console.log(`Error: Input file ${inputFilePath} is empty or missing.`);
	process.exit(1);
}

const modulePath = `../day${dayStr}/q${part}.ts`;
try {
	const module = await import(modulePath);
	const funcName = `solve`;
	const solveFunction = module[funcName];
	
	if (!solveFunction) {
		console.log(`Error: Function ${funcName} not found in module ${modulePath}`);
		process.exit(1);
	}
	
	const timeStart = performance.now();
	const result = await solveFunction(inputData);
	console.log(`\nResult: ${result}`);
	const timeEnd = performance.now();
	console.log(`Time taken: ${(timeEnd - timeStart).toFixed(3)} ms`);
} catch (e) {
	console.log(`Error importing module ${modulePath}: ${e}`);
	process.exit(1);
}