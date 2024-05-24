<script>
  import { onMount } from 'svelte';
  import CommandPacket from '$lib/packets/CommandPacket.svelte';
    import ResponsePacket from '$lib/packets/ResponsePacket.svelte';

	/** @type {import('./$types').PageData} */
	export let data;
  let packets = [];

  onMount(() => {
    if (!data.isFilenameValid) {
      window.location.href = "pcap";
    }

    const commands = JSON.parse(data.commandsJson);
    const responses = JSON.parse(data.responsesJson);

    for (let command of commands) {
      command.type = "CommandPacket";
      packets.push(command);
    }

    for (let response of responses) {
      response.type = "ResponsePacket";
      packets.push(response);
    }

    packets.sort((packet1, packet2) => (packet1.pcapIndex - packet2.pcapIndex));
    packets = packets; // Svelte reactivity
  });
</script>

<svelte:head>
</svelte:head>

{#if data.isFilenameValid}
  <section>
    <h3><strong>Pcap Viewer</strong> | {data.filename}</h3>
  </section>
{/if}

{#each packets as packet}
{#if packet.type === "CommandPacket"}
<CommandPacket packet={packet} />
{:else if packet.type === "ResponsePacket"}
<ResponsePacket packet={packet} />
{/if}
{/each}

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}
</style>
