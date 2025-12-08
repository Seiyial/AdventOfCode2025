export const solve = (inputData: string) => {
	const lines = inputData.split('\n').filter(line => line.length > 0);
	const colSpec = getColPositions(lines.splice(lines.length - 1, 1)[0]!)
	return colSpec.reduce((sum, { startIdx, endIdxExcl, op }) => {
		return sum + (
			op === '+'
				? lines.reduce((acc, row, idx) => idx ? Number(row.slice(startIdx, endIdxExcl)) + acc : Number(row.slice(startIdx, endIdxExcl)), 0)
				: lines.reduce((acc, row, idx) => idx ? Number(row.slice(startIdx, endIdxExcl)) * acc : Number(row.slice(startIdx, endIdxExcl)), 0)
		)
	}, 0)
}

const getColPositions = (lastLine: string) => {
	return lastLine
		.split('')
		.reduce((opPosIndexes, cur, curIndex, line) => {
			if (cur !== ' ') {
				if (opPosIndexes.length) {
					opPosIndexes[opPosIndexes.length - 1]!.endIdxExcl = curIndex
				}
				opPosIndexes.push({ op: cur as '*' | '+', startIdx: curIndex, endIdxExcl: Infinity })
			}
			return opPosIndexes
		}, <{startIdx: number, op: '+' | '*', endIdxExcl: number}[]>[])
}