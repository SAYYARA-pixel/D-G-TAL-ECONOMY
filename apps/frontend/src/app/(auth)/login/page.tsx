'use client';

import { FormEvent, useState } from 'react';
import { useRouter } from 'next/navigation';

import { apiFetch } from '@/lib/api';

export default function LoginPage() {
  const router = useRouter();
  const [email, setEmail] = useState('admin@economy.gov.az');
  const [password, setPassword] = useState('Admin123!');

  async function submit(e: FormEvent) {
    e.preventDefault();
    const res = await apiFetch('/auth/login', undefined, { method: 'POST', body: JSON.stringify({ email, password }) });
    localStorage.setItem('token', res.access_token);
    router.push('/dashboard');
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-100">
      <form onSubmit={submit} className="bg-white p-6 rounded-xl shadow-sm w-96 space-y-3">
        <h1 className="font-semibold text-xl">Daxil ol</h1>
        <input className="w-full border rounded p-2" value={email} onChange={(e) => setEmail(e.target.value)} />
        <input className="w-full border rounded p-2" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <button className="w-full bg-gov-700 text-white rounded p-2" type="submit">Giriş</button>
      </form>
    </div>
  );
}
