import Card from "../components/Card";

export default function Tokens() {
  return (
    <div className="p-6">
      <Card title="Token Management">
        <button className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
          Generate Token
        </button>
      </Card>
    </div>
  );
}
