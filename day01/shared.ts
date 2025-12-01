import { chain, math } from '../common'

export enum Passing {
	Include = 1,
	DontInclude = 0
}

export const crunchIt = (inputData: string, countPassing: Passing) => (
	inputData
		.split('\n')
		.map((spec): [turn: number, fullSpins: number] => {
			const delta = Number(spec.slice(1)) * (spec.at(0) === 'L' ? -1 : 1)
			return [
				delta % 100,
				chain(delta, math.divideBy(100), Math.trunc, Math.abs)
				// Vanilla JS: Math.abs(Math.trunc(delta / 100))
			]
		})
		.reduce((acc, [delta, fullSpins]) => {
			return (
				acc.pos = acc.pos || (delta < 0 ? 100 : 0),
				acc.count += fullSpins,
				acc.pos += delta,
				acc.pos === 0 && (acc.count += 1),
				acc.pos === 100 && (acc.pos -= 100, acc.count += 1),
				acc.pos > 100 && (acc.pos -= 100, countPassing && (acc.count += 1)),
				acc.pos < 0 && (acc.pos += 100, countPassing && (acc.count += 1)),
				acc
			)
		}, { count: 0, pos: 50 })
		.count
)

export const solveQ1 = (input: string) => crunchIt(input, Passing.DontInclude)
export const solveQ2 = (input: string) => crunchIt(input, Passing.Include)
