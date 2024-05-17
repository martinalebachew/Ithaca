/** @type {import('./$types').PageServerLoad} */
export async function load({ params, url }) {
	let filename = url.searchParams.get('filename');

	return {
		filename: filename
	};
}