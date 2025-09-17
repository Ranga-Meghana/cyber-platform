export default function Navbar() {
  return (
    <nav className="navbar">
      <h1 className="navbar-title">Cyber Platform</h1>
      <div className="navbar-links">
        <a href="/dashboard" className="navbar-link">Dashboard</a>
        <a href="/users" className="navbar-link">Users</a>
        <a href="/tokens" className="navbar-link">Tokens</a>
        <a href="/decoys" className="navbar-link">Decoys</a>
        <a href="/replay" className="navbar-link">Replay</a>
        <a href="/attribution" className="navbar-link">Attribution</a>
      </div>
    </nav>
  );
}