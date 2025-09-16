import Card from "../components/Card";

export default function Users() {
  return (
    <div className="p-6">
      <Card title="Users List">
        <ul className="list-disc pl-5">
          <li>User A</li>
          <li>User B</li>
          <li>User C</li>
        </ul>
      </Card>
    </div>
  );
}
