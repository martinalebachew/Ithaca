<script>
	import RavKavImage from '$lib/images/ravkav-envelope.png';
</script>

<svelte:head>
</svelte:head>

<section>
	<h3><strong>Ithaca Web Portal</strong> | RavKav Research</h3>
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
</style>
