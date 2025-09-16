export default function Navbar() {
  return (
    <nav className="bg-gray-900 text-white px-6 py-4 flex justify-between items-center shadow-md">
      <h1 className="text-xl font-bold">Cyber Platform</h1>
      <div className="flex gap-6">
        <a href="/dashboard" className="hover:text-gray-300">Dashboard</a>
        <a href="/users" className="hover:text-gray-300">Users</a>
        <a href="/tokens" className="hover:text-gray-300">Tokens</a>
        <a href="/decoys" className="hover:text-gray-300">Decoys</a>
        <a href="/replay" className="hover:text-gray-300">Replay</a>
        <a href="/attribution" className="hover:text-gray-300">Attribution</a>
      </div>
    </nav>
  );
}
