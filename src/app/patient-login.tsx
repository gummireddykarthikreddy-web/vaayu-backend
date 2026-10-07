import React from 'react';
import { useRouter } from 'expo-router';

export default function PatientLoginScreen() {
  const router = useRouter();

  return (
    <div style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', backgroundColor: '#020617', overflowY: 'auto' }}>
      <style>{`
        @keyframes scanline {
          0% { transform: translateY(-100%); }
          100% { transform: translateY(100%); }
        }
        @keyframes pulseFingerprint {
          0%, 100% { opacity: 0.5; filter: drop-shadow(0 0 5px #00E5FF); }
          50% { opacity: 1; filter: drop-shadow(0 0 20px #00E5FF); }
        }
      `}</style>

      <div style={{
        background: 'linear-gradient(145deg, rgba(15,23,42,0.8), rgba(2,6,23,0.95))',
        border: '1px solid rgba(0, 229, 255, 0.4)',
        boxShadow: '0 0 50px rgba(0,229,255,0.1)',
        borderRadius: 24,
        padding: 40,
        width: '100%',
        maxWidth: 500,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: 30
      }}>
        
        {/* Biometric Icon */}
        <div style={{ position: 'relative', width: 80, height: 80, display: 'flex', justifyContent: 'center', alignItems: 'center', animation: 'pulseFingerprint 2s infinite' }}>
          <div style={{ fontSize: 60, color: '#00E5FF' }}>◎</div>
          <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', borderTop: '2px solid #00E5FF', animation: 'scanline 2s linear infinite', opacity: 0.8 }} />
        </div>

        {/* Title */}
        <div style={{ textAlign: 'center' }}>
          <h1 style={{ margin: 0, fontSize: 24, fontWeight: '900', color: '#00E5FF', textTransform: 'uppercase', letterSpacing: 3, textShadow: '0 0 15px rgba(0,229,255,0.8)' }}>
            Vaayu Patient Authentication
          </h1>
          <p style={{ margin: '10px 0 0 0', color: '#94A3B8', fontSize: 12, letterSpacing: 1 }}>SECURE BIOMETRIC CLEARANCE REQUIRED</p>
        </div>

        {/* Input */}
        <div style={{ width: '100%' }}>
          <input 
            type="text" 
            placeholder="ENTER VAAYU-XXXXX"
            style={{
              background: 'rgba(0,0,0,0.5)',
              border: '1px solid #38BDF8',
              color: '#FFF',
              padding: 16,
              width: '100%',
              fontSize: 18,
              textAlign: 'center',
              letterSpacing: 2,
              outline: 'none',
              boxShadow: 'inset 0 0 10px rgba(56,189,248,0.2)',
              borderRadius: 12
            }}
          />
        </div>

        {/* Button */}
        <button 
          onClick={() => router.push('/patient')}
          style={{
            background: 'linear-gradient(90deg, #0284C7, #00E5FF)',
            border: 'none',
            color: '#0F172A',
            padding: '18px 30px',
            width: '100%',
            fontSize: 16,
            fontWeight: '900',
            letterSpacing: 2,
            textTransform: 'uppercase',
            borderRadius: 12,
            cursor: 'pointer',
            boxShadow: '0 0 20px rgba(0,229,255,0.5)',
            transition: 'all 0.3s ease'
          }}
          onMouseOver={(e) => e.currentTarget.style.boxShadow = '0 0 35px rgba(0,229,255,0.8)'}
          onMouseOut={(e) => e.currentTarget.style.boxShadow = '0 0 20px rgba(0,229,255,0.5)'}
        >
          [ INITIATE SECURE BIOMETRIC LOGIN ]
        </button>

      </div>
    </div>
  );
}
