import { ReactNode } from 'react';

export function TableCard({ title, children }: { title: string; children: ReactNode }) {
  return (
    <section className="bg-white rounded-xl shadow-sm border border-slate-200 p-4">
      <h2 className="font-semibold text-lg mb-3">{title}</h2>
      <div className="overflow-auto">{children}</div>
    </section>
  );
}
