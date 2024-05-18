<script>
  import { onMount } from 'svelte';

	/** @type {import('./$types').PageData} */
	export let data;

  onMount(() => {
    if (!data.isFilenameValid) {
      window.location.href = "pcap";
    }
  });
</script>

<svelte:head>
</svelte:head>

{#if data.isFilenameValid}
  <section>
    <h3><strong>Pcap Viewer</strong> | {data.filename}</h3>
  </section>
{/if}

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}
</style>
