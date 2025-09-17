import Card from "../components/Card";

export default function Users() {
  return (
    <div className="page-container">
      <Card title="Users List">
        <ul className="list-disc">
          <li>User A</li>
          <li>User B</li>
          <li>User C</li>
        </ul>
      </Card>
    </div>
  );
}