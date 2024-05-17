<script>
	import { Button, Label, Select } from 'flowbite-svelte';

	/** @type {import('./$types').PageData} */
	export let data;
	let selected;
</script>

<svelte:head>
</svelte:head>

<section>
	<h3><strong>Pcap Loader</strong></h3>
	<p>Uploading is not supported. Add .pcap files manually to the server.</p>

	<Label>
		<Select items={data.pcapItems} bind:value={selected} placeholder="Choose a .pcap file to load..." />
	</Label>

	<div class="load-button-container">
		<Button>Load</Button>
	</div>
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	.load-button-container {
		margin-top: 3px;
	}
</style>
