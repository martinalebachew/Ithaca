<script>
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte';
  import { hex, decimal, hexify64 } from '$lib/helpers/shared/strings';

  export let packet;
</script>

<Table hoverable={true}>
  <TableHead>
    <TableHeadCell class="w-5">NO</TableHeadCell>
    <TableHeadCell class="w-5">CLA</TableHeadCell>
    <TableHeadCell class="w-5">INS</TableHeadCell>
    <TableHeadCell class="w-5">P1</TableHeadCell>
    <TableHeadCell class="w-5">P2</TableHeadCell>
    <TableHeadCell class="w-5">Lc</TableHeadCell>
    <TableHeadCell class="w-50">Data</TableHeadCell>
    <TableHeadCell class="w-5">Le</TableHeadCell>
  </TableHead>
  <TableBody>
    <TableBodyRow>
      <TableBodyCell>{decimal(packet.pcapIndex)}</TableBodyCell>
      <TableBodyCell>{hex(packet.cla)}</TableBodyCell>
      <TableBodyCell>{hex(packet.ins)}</TableBodyCell>
      <TableBodyCell>{hex(packet.p1)}</TableBodyCell>
      <TableBodyCell>{hex(packet.p2)}</TableBodyCell>
      <TableBodyCell>{hex(packet.lc)}</TableBodyCell>
      <TableBodyCell>{hexify64(packet.data)}</TableBodyCell>
      <TableBodyCell>{hex(packet.le)}</TableBodyCell>
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