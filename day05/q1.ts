export const solve = (inputData: string) => {
	const [top, bottom] = inputData.split('\n\n')
	const ranges = top!.split('\n').map((ln) => ln.split('-').map((i) => Number(i)))
	return bottom!.split('\n').map((ing) => Number(ing)).reduce((count, ing) => (
		ranges.some(([min, max]) => ing >= min! && ing <= max!) ? count + 1 : count
	), 0)
}
