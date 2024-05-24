<script>
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte';
  import { hex, decimal, hexify64 } from '$lib/helpers/shared/strings';

  export let packet;
</script>

<Table hoverable={true}>
  <TableHead>
    <TableHeadCell class="w-5">NO</TableHeadCell>
    <TableHeadCell class="w-50">Data</TableHeadCell>
    <TableHeadCell class="w-5">SW1</TableHeadCell>
    <TableHeadCell class="w-5">SW2</TableHeadCell>
  </TableHead>
  <TableBody>
    <TableBodyRow>
      <TableBodyCell>{decimal(packet.pcapIndex)}</TableBodyCell>
      <TableBodyCell>{hexify64(packet.data)}</TableBodyCell>
      <TableBodyCell>{hex(packet.sw1)}</TableBodyCell>
      <TableBodyCell>{hex(packet.sw2)}</TableBodyCell>
    </TableBodyRow>
  </TableBody>
  <TableBody>
  </TableBody>
</Table>
<Table>
  <TableBodyRow>
    <TableBodyCell>{packet.description}</TableBodyCell>
  </TableBodyRow>
</Table>