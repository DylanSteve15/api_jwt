#!/bin/bash
BASE_URL="http://localhost:5000"

echo "============================"
echo "📌 INICIANDO PRUEBAS API"
echo "============================"

# === Registro de usuario ===
echo "📌 Registrando usuario..."
curl -s -X POST $BASE_URL/users/register \
    -H "Content-Type: application/json" \
    -d '{"username": "usuario1", "password": "password1"}'
echo -e "\n---"

# === Login y captura de token ===
echo "📌 Login usuario..."
TOKEN=$(curl -s -X POST $BASE_URL/users/login \
    -H "Content-Type: application/json" \
    -d '{"username": "usuario1", "password": "password1"}' \
    | python3 -c "import sys, json; print(json.load(sys.stdin).get('access_token', ''))")

if [ -z "$TOKEN" ]; then
  echo "❌ Error: No se obtuvo token"
  exit 1
fi
echo "✅ Token obtenido"
echo -e "\n---"

# === Listado de usuarios ===
echo "📌 Listando usuarios..."
curl -s -X GET $BASE_URL/users/ \
    -H "Authorization: Bearer $TOKEN" | jq .
echo -e "\n---"

# === Crear estudiante ===
echo "📌 Creando estudiante..."
curl -s -X POST $BASE_URL/estudiantes \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"nombre":"Dylan Rodriguez","carrera":"Ingeniería de Sistemas"}' | jq .
echo -e "\n---"

# === Listar estudiantes ===
echo "📌 Listando estudiantes..."
curl -s -X GET $BASE_URL/estudiantes \
    -H "Authorization: Bearer $TOKEN" | jq .
echo -e "\n---"

# === Eliminar estudiante (ID=1 ejemplo) ===
echo "📌 Eliminando estudiante ID=1..."
curl -s -X DELETE $BASE_URL/estudiantes/1 \
    -H "Authorization: Bearer $TOKEN" | jq .
echo -e "\n---"

# === Crear horario ===
echo "📌 Creando horario..."
curl -s -X POST $BASE_URL/horarios \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"estudiante_id":1,"materia":"Bases de Datos","hora":"08:00"}' | jq .
echo -e "\n---"

# === Listar horarios ===
echo "📌 Listando horarios..."
curl -s -X GET $BASE_URL/horarios \
    -H "Authorization: Bearer $TOKEN" | jq .
echo -e "\n---"

# === Eliminar horario (ID=1 ejemplo) ===
echo "📌 Eliminando horario ID=1..."
curl -s -X DELETE $BASE_URL/horarios/1 \
    -H "Authorization: Bearer $TOKEN" | jq .
echo -e "\n---"

echo "✅ PRUEBAS FINALIZADAS"
