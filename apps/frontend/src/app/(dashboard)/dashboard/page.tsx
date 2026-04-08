export default function DashboardPage() {
  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-semibold">İcra paneli</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {[
          ['Aktiv layihələr', '12'],
          ['Aşkarlanmış hüquqi risklər', '37'],
          ['Sahibkar yükünün azalması', '42%'],
        ].map(([k, v]) => (
          <div key={k} className="bg-white border rounded-xl p-4 shadow-sm">
            <p className="text-sm text-slate-500">{k}</p>
            <p className="text-2xl font-semibold">{v}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
