
/** max chain 5. **Does not support type parameter functions.** */
export function chain<A, B>(input: A, fn1: (arg: A) => B): B
export function chain<A, B, C>(input: A, fn1: (arg: A) => B, fn2: (arg: B) => C): C
export function chain<A, B, C, D>(input: A, fn1: (arg: A) => B, fn2: (arg: B) => C, fn3: (arg: C) => D): D
export function chain<A, B, C, D, E>(input: A, fn1: (arg: A) => B, fn2: (arg: B) => C, fn3: (arg: C) => D, fn4: (arg: D) => E): E
export function chain<A, B, C, D, E, F>(input: A, fn1: (arg: A) => B, fn2: (arg: B) => C, fn3: (arg: C) => D, fn4: (arg: D) => E, fn5: (arg: E) => F): F
export function chain(input: unknown, ...fns: Array<(arg: unknown) => unknown>): unknown {
	return fns.reduce((acc, fn) => fn(acc), input)
}

export namespace math {
	export const clamp = (num: number, min: number, max: number) => Math.min(Math.max(num, min), max)
	export const lerp = (a: number, b: number, t: number) => a + (b - a) * t
	export const percentify = (part: number, total: number, numDP: number = 1) => (total === 0 ? 0 : (part / total) * 100).toFixed(numDP)
	export const add = (addBy: number) => (num: number) => num + addBy
	export const subtract = (subtBy: number) => (num: number) => num - subtBy
	export const multiply = (multBy: number) => (num: number) => num * multBy
	export const divideBy = (divBy: number) => (num: number) => num / divBy
	export const powBy = (expBy: number) => (num: number) => num ** expBy
}