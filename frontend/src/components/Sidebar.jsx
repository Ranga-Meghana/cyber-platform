export default function Sidebar() {
  return (
    <aside className="sidebar">
      <h2 className="sidebar-title">Menu</h2>
      <a href="/dashboard" className="sidebar-link">Dashboard</a>
      <a href="/users" className="sidebar-link">Users</a>
      <a href="/tokens" className="sidebar-link">Tokens</a>
      <a href="/decoys" className="sidebar-link">Decoys</a>
      <a href="/replay" className="sidebar-link">Replay</a>
      <a href="/attribution" className="sidebar-link">Attribution</a>
    </aside>
  );
}