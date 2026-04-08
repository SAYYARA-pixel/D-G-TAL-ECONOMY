'use client';
import { useEffect, useState } from 'react';
import { TableCard } from '@/components/table-card';
import { apiFetch } from '@/lib/api';

export default function Page() {
  const [items, setItems] = useState<any[]>([]);
  useEffect(() => { apiFetch('/registry/burden-assessments', localStorage.getItem('token') || '').then(setItems).catch(console.error); }, []);
  return <TableCard title="Uyğunluq yükü kalkulyatoru"><pre>{JSON.stringify(items, null, 2)}</pre></TableCard>;
}
