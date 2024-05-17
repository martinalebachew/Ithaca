<script>
	import RavKavImage from '$lib/images/ravkav-envelope.png';
</script>

<svelte:head>
</svelte:head>

<section>
	<h1>Ithaca Web Portal // RavKav Research</h1>
	<p>Choose an operation mode from the menu above.</p>
	
	<img src={RavKavImage} alt="RavKav" />
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}
</style>
