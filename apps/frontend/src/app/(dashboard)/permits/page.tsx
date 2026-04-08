'use client';
import { useEffect, useState } from 'react';
import { TableCard } from '@/components/table-card';
import { apiFetch } from '@/lib/api';

export default function Page() {
  const [items, setItems] = useState<any[]>([]);
  useEffect(() => { apiFetch('/registry/permits', localStorage.getItem('token') || '').then(setItems).catch(console.error); }, []);
  return <TableCard title="Lisenziya və icazə naviqatoru"><pre>{JSON.stringify(items, null, 2)}</pre></TableCard>;
}
