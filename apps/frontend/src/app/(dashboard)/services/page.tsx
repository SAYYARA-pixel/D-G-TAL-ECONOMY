'use client';
import { useEffect, useState } from 'react';
import { TableCard } from '@/components/table-card';
import { apiFetch } from '@/lib/api';

export default function Page() {
  const [items, setItems] = useState<any[]>([]);
  useEffect(() => { apiFetch('/registry/services', localStorage.getItem('token') || '').then(setItems).catch(console.error); }, []);
  return <TableCard title="Dövlət xidmətləri xəritəsi"><pre>{JSON.stringify(items, null, 2)}</pre></TableCard>;
}
