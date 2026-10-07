import React from 'react';
import { useRouter } from 'expo-router';

export default function DoctorLoginScreen() {
  const router = useRouter();

  return (
    <div style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', backgroundColor: '#020617', overflowY: 'auto' }}>
      <style>{`
        @keyframes pulseGold {
          0%, 100% { opacity: 0.7; filter: drop-shadow(0 0 10px #F59E0B); }
          50% { opacity: 1; filter: drop-shadow(0 0 25px #F59E0B); }
        }
      `}</style>

      <div style={{
        background: 'linear-gradient(145deg, rgba(10,10,10,0.9), rgba(20,20,20,0.95))',
        border: '1px solid rgba(250, 204, 21, 0.4)',
        boxShadow: '0 0 50px rgba(250,204,21,0.1)',
        borderRadius: 24,
        padding: 40,
        width: '100%',
        maxWidth: 500,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: 30
      }}>
        
        {/* Security Icon */}
        <div style={{ position: 'relative', width: 80, height: 80, display: 'flex', justifyContent: 'center', alignItems: 'center', animation: 'pulseGold 3s infinite' }}>
          <div style={{ fontSize: 60, color: '#FACC15' }}>⬡</div>
        </div>

        {/* Title */}
        <div style={{ textAlign: 'center' }}>
          <h1 style={{ margin: 0, fontSize: 24, fontWeight: '900', color: '#FACC15', textTransform: 'uppercase', letterSpacing: 3, textShadow: '0 0 15px rgba(250,204,21,0.6)' }}>
            Doctor Surgical Vault Access
          </h1>
          <p style={{ margin: '10px 0 0 0', color: '#A1A1AA', fontSize: 12, letterSpacing: 1 }}>RESTRICTED SECTOR • LEVEL-4 CLEARANCE</p>
        </div>

        {/* Inputs */}
        <div style={{ width: '100%', display: 'flex', flexDirection: 'column', gap: 16 }}>
          <input 
            type="text" 
            placeholder="MEDICAL LICENSE ID"
            style={{
              background: 'rgba(0,0,0,0.6)',
              border: '1px solid #F59E0B',
              color: '#FFF',
              padding: 16,
              width: '100%',
              fontSize: 16,
              textAlign: 'center',
              letterSpacing: 2,
              outline: 'none',
              boxShadow: 'inset 0 0 10px rgba(245,158,11,0.1)',
              borderRadius: 12
            }}
          />
          <input 
            type="password" 
            placeholder="SECURE CLEARANCE PIN"
            style={{
              background: 'rgba(0,0,0,0.6)',
              border: '1px solid #F59E0B',
              color: '#FFF',
              padding: 16,
              width: '100%',
              fontSize: 16,
              textAlign: 'center',
              letterSpacing: 4,
              outline: 'none',
              boxShadow: 'inset 0 0 10px rgba(245,158,11,0.1)',
              borderRadius: 12
            }}
          />
        </div>

        {/* Button */}
        <button 
          onClick={() => router.push('/doctor-patient-select')}
          style={{
            background: 'linear-gradient(90deg, #B45309, #FACC15)',
            border: 'none',
            color: '#000',
            padding: '18px 30px',
            width: '100%',
            fontSize: 16,
            fontWeight: '900',
            letterSpacing: 2,
            textTransform: 'uppercase',
            borderRadius: 12,
            cursor: 'pointer',
            boxShadow: '0 0 20px rgba(250,204,21,0.4)',
            transition: 'all 0.3s ease'
          }}
          onMouseOver={(e) => e.currentTarget.style.boxShadow = '0 0 35px rgba(250,204,21,0.7)'}
          onMouseOut={(e) => e.currentTarget.style.boxShadow = '0 0 20px rgba(250,204,21,0.4)'}
        >
          [ AUTHORIZE LEVEL-4 ACCESS ]
        </button>

      </div>
    </div>
  );
}
