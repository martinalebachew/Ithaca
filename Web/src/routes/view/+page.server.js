import { isParamValid } from '$lib/helpers/shared/params';
import { parsePcapFile } from '$lib/helpers/server/bridge';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params, url }) {
	const filename = url.searchParams.get('filename');

	if (!isParamValid(filename)) {
		return {
			isFilenameValid: false,
			filename: filename
		};
	}

	const [commands, responses] = parsePcapFile(filename);

	return {
		isFilenameValid: true,
		filename: filename,
		commandsJson: JSON.stringify(commands),
		responsesJson: JSON.stringify(responses)
	}
}