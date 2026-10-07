-- Enable UUID generation for secure, non-guessable IDs
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- 1. Identity Layer
CREATE TABLE patients (
    patient_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    abha_id VARCHAR(17) UNIQUE NOT NULL,
    name_hash VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE doctors (
    doctor_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    license_number VARCHAR(50) UNIQUE NOT NULL,
    specialty VARCHAR(100)
);

-- 2. Diagnostics Layer (JSONB for complex lab data)
CREATE TABLE lab_reports (
    report_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    patient_id UUID REFERENCES patients(patient_id) ON DELETE CASCADE,
    report_type VARCHAR(50) NOT NULL,
    metrics JSONB NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Security Layer
-- This enforces that API queries can only fetch data for the logged-in user
ALTER TABLE lab_reports ENABLE ROW LEVEL SECURITY;

CREATE POLICY patient_isolation_policy ON lab_reports
    FOR SELECT
    USING (patient_id = current_setting('app.current_patient_id', true)::UUID);