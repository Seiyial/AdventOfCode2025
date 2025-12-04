// this is a debug reproduction of someone else (H)'s method, not ours

const matches = (numStr: string) => {
	const substringCounts: Record<string, number> = {}
	for (let winSize = 1; winSize <= (numStr.length / 2); winSize++) {
		for (let winStart = 0; winStart <= numStr.length - winSize && winStart <= numStr.length / 2; winStart++) {
			substringCounts[numStr.slice(winStart, winStart + winSize)] = 0
		}
	}
	// console.log(Object.keys(substringCounts))

	for (const compareKey in substringCounts) {
		if (!Object.hasOwn(substringCounts, compareKey)) continue

		const size = compareKey.length
		for (let winStart = 0; winStart <= numStr.length - compareKey.length; winStart += compareKey.length) {
			const currentSeq = numStr.slice(winStart, winStart + compareKey.length)

			if (currentSeq !== compareKey) {
				substringCounts[compareKey] = 0; break
			}

			if ((winStart + compareKey.length) > (numStr.length - compareKey.length)) {
				// check end
				const currentSeqEnd = numStr.slice(numStr.length - compareKey.length, winStart + compareKey.length)
				if (currentSeqEnd !== compareKey) {
					substringCounts[compareKey] = 0; break
				}
			}

			substringCounts[compareKey]!++
		}
	}

	if (Object.values(substringCounts).some((c) => c > 1)) {
		const matched = Object.entries(substringCounts).filter(([k, v]) => v > 1)
		if (matched.length > 0) console.log(numStr, 'via', matched[0]![0])
		return true
	} else {
		return false
	}
}

export const solve = (input: string) => {
	return input.split(',').reduce((acc, item) => {
		const [start, end] = item.split('-').map(Number)
		for (let i = start!; i <= end!; i++) {
			if (matches(String(i))) acc += i
		}
		return acc
	}, 0)
}