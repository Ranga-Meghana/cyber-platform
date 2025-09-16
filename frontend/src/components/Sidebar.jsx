export default function Sidebar() {
  return (
    <aside className="bg-gray-800 text-white w-60 h-screen p-6 flex flex-col gap-4">
      <h2 className="text-lg font-semibold">Menu</h2>
      <a href="/dashboard" className="hover:bg-gray-700 rounded p-2">Dashboard</a>
      <a href="/users" className="hover:bg-gray-700 rounded p-2">Users</a>
      <a href="/tokens" className="hover:bg-gray-700 rounded p-2">Tokens</a>
      <a href="/decoys" className="hover:bg-gray-700 rounded p-2">Decoys</a>
      <a href="/replay" className="hover:bg-gray-700 rounded p-2">Replay</a>
      <a href="/attribution" className="hover:bg-gray-700 rounded p-2">Attribution</a>
    </aside>
  );
}
