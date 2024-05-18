import { isParamValid } from '$lib/helpers/shared/params';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params, url }) {
	let filename = url.searchParams.get('filename');

	if (!isParamValid(filename)) {
		return {
			isFilenameValid: false,
			filename: filename
		};
	}
	
	/*
	 * TODO: Communicate with parser
	 */

	return {
		isFilenameValid: true,
		filename: filename
	}
}