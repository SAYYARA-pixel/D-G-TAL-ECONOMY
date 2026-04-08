import Link from 'next/link';

const links = [
  ['dashboard', '/dashboard'],
  ['hüquqi sənədlər', '/legal-documents'],
  ['xidmətlər', '/services'],
  ['icazələr', '/permits'],
  ['inzibati yük', '/burden-assessments'],
  ['risk indikatorları', '/risk-indicators'],
  ['AI köməkçi', '/ai-assistant'],
  ['admin', '/admin'],
];

export function Nav() {
  return (
    <aside className="w-72 bg-gov-900 text-white min-h-screen p-5">
      <h1 className="font-semibold text-xl mb-6">İqtisadiyyat Nazirliyi Platforması</h1>
      <ul className="space-y-3 text-sm">
        {links.map(([label, href]) => (
          <li key={href}>
            <Link className="block rounded px-3 py-2 hover:bg-gov-700" href={href}>
              {label}
            </Link>
          </li>
        ))}
      </ul>
    </aside>
  );
}
