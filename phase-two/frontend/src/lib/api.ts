const API_BASE = process.env.NEXT_PUBLIC_API_BASE || "http://127.0.0.1:8000";

async function request(path: string, options: RequestInit = {}, token?: string) {
  const headers: Record<string, string> = { ...(options.headers as Record<string, string>) };
  if (!headers["Content-Type"] && options.body && !(options.body instanceof FormData)) {
    headers["Content-Type"] = "application/json";
  }
  if (token) headers.Authorization = `Bearer ${token}`;

  const res = await fetch(`${API_BASE}${path}`, { ...options, headers });
  const text = await res.text();
  if (!res.ok) {
    throw new Error(text || res.statusText);
  }
  return text ? JSON.parse(text) : null;
}

export async function signup(email: string, password: string) {
  return request("/auth/signup", {
    method: "POST",
    body: JSON.stringify({ email, password }),
  });
}

export async function login(email: string, password: string) {
  const form = new URLSearchParams({ username: email, password });
  return request(
    "/auth/login",
    {
      method: "POST",
      body: form,
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
    },
    undefined
  );
}

export async function listTasks(token: string, userId: number) {
  return request(`/api/${userId}/tasks`, { method: "GET" }, token);
}

export async function createTask(token: string, userId: number, title: string, description = "") {
  return request(
    `/api/${userId}/tasks`,
    { method: "POST", body: JSON.stringify({ title, description }) },
    token
  );
}

export async function toggleTask(token: string, userId: number, id: number) {
  return request(`/api/${userId}/tasks/${id}/complete`, { method: "PATCH" }, token);
}

export async function updateTask(
  token: string,
  userId: number,
  id: number,
  data: Partial<{ title: string; description: string; status: "open" | "done" }>
) {
  return request(`/api/${userId}/tasks/${id}`, { method: "PATCH", body: JSON.stringify(data) }, token);
}

export async function deleteTask(token: string, userId: number, id: number) {
  return request(`/api/${userId}/tasks/${id}`, { method: "DELETE" }, token);
}
