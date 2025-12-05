export const solve = (inputData: string) => {
	return inputData.split('\n\n')[0]!.split('\n').map((ln) => ln.split('-').map(Number))
		.reduce((sum, [min, max]) => sum + (max! - min! + 1), 0)
}