FROM python:3.12-slim

WORKDIR /backend

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  wget \
  gnupg \
  lsb-release \
  netcat-openbsd \
  && echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" \
  > /etc/apt/sources.list.d/pgdg.list \
  && wget -qO - https://www.postgresql.org/media/keys/ACCC4CF8.asc \
  | gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
  postgresql-client-18 \
  && rm -rf /var/lib/apt/lists/*


COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen

ENV PATH="/backend/.venv/bin:$PATH"

COPY . .

EXPOSE 8000

ENTRYPOINT ["./scripts/entrypoint.sh"]