import { env } from '$env/dynamic/private';
import { getPcapFiles } from '$lib/helpers/server/files';
import { arrayToListItems } from '$lib/helpers/shared/data';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params }) {
	return {
		pcapItems: arrayToListItems(getPcapFiles(env.PCAP_FILES_DIRECTORY))
	};
}