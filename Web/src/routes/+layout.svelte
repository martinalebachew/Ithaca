<script>
	import '$lib/styles/index.css';
	import { Nav } from '$lib/nav';
</script>

<svelte:head>
	<title>Ithaca Web Portal</title>
</svelte:head>

<div class="app">
	<Nav></Nav>

	<main>
		<slot></slot>
	</main>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
	}
</style>