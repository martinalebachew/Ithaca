import { isParamValid } from '$lib/helpers/shared/params';
import { parsePcapFile } from '$lib/helpers/server/bridge';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params, url }) {
	let filename = url.searchParams.get('filename');

	if (!isParamValid(filename)) {
		return {
			isFilenameValid: false,
			filename: filename
		};
	}

	return {
		isFilenameValid: true,
		filename: filename,
		packetsJson: JSON.stringify(parsePcapFile(filename))
	}
}