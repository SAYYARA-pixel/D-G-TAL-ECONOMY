'use client';

import { useEffect, useState } from 'react';

import { TableCard } from '@/components/table-card';
import { apiFetch } from '@/lib/api';

type LegalDocument = {
  id: number;
  title_az: string;
  institution: string;
  status: string;
};

type Version = {
  id: number;
  legal_document_id: number;
  version_label: string;
  content: string;
};

type Finding = {
  id: number;
  document_version_id: number;
  norma_ref: string;
  issue: string;
  risk_level: string;
  recommendation: string;
  rationale: string;
};

const token = typeof window !== 'undefined' ? localStorage.getItem('token') || '' : '';

export default function LegalDocumentsPage() {
  const [documents, setDocuments] = useState<LegalDocument[]>([]);
  const [versions, setVersions] = useState<Version[]>([]);
  const [findings, setFindings] = useState<Finding[]>([]);

  useEffect(() => {
    apiFetch('/legal/documents', token).then(setDocuments).catch(console.error);
  }, []);

  async function loadVersions(id: number) {
    const result = await apiFetch(`/legal/versions?document_id=${id}`, token);
    setVersions(result);
    setFindings([]);
  }

  async function loadFindings(id: number) {
    const result = await apiFetch(`/legal/findings?version_id=${id}`, token);
    setFindings(result);
  }

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-semibold">Hüquqi Analiz İş Sahəsi</h1>
      <TableCard title="Sənədlər">
        <table className="w-full text-sm">
          <thead>
            <tr className="text-left border-b"><th>Başlıq</th><th>Qurum</th><th>Status</th></tr>
          </thead>
          <tbody>
            {documents.map((d) => (
              <tr key={d.id} className="border-b hover:bg-slate-50 cursor-pointer" onClick={() => loadVersions(d.id)}>
                <td>{d.title_az}</td><td>{d.institution}</td><td>{d.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </TableCard>
      <TableCard title="Versiyalar">
        <table className="w-full text-sm">
          <thead><tr className="text-left border-b"><th>Versiya</th><th>Mətn</th></tr></thead>
          <tbody>
            {versions.map((v) => (
              <tr key={v.id} className="border-b hover:bg-slate-50 cursor-pointer" onClick={() => loadFindings(v.id)}>
                <td>{v.version_label}</td><td className="truncate max-w-72">{v.content}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </TableCard>
      <TableCard title="Ekspert rəyləri (norma / problem / risk / tövsiyə)">
        <table className="w-full text-sm">
          <thead><tr className="text-left border-b"><th>Norma</th><th>Problem</th><th>Risk</th><th>Tövsiyə</th></tr></thead>
          <tbody>
            {findings.map((f) => (
              <tr key={f.id} className="border-b"><td>{f.norma_ref}</td><td>{f.issue}</td><td>{f.risk_level}</td><td>{f.recommendation}</td></tr>
            ))}
          </tbody>
        </table>
      </TableCard>
    </div>
  );
}
