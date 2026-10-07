import React from 'react';
import { useRouter } from 'expo-router';

export default function DoctorPatientSelectScreen() {
  const router = useRouter();

  return (
    <div style={{ minHeight: '100vh', padding: 40, backgroundColor: '#020617', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      
      {/* Title */}
      <h1 style={{ margin: '0 0 40px 0', fontSize: 32, fontWeight: '900', color: '#38BDF8', textTransform: 'uppercase', letterSpacing: 4, textShadow: '0 0 20px rgba(56,189,248,0.6)', textAlign: 'center' }}>
        Select Patient Telemetry Target
      </h1>

      <div style={{
        background: 'linear-gradient(145deg, rgba(15,23,42,0.8), rgba(5,10,20,0.95))',
        border: '1px solid rgba(56,189,248,0.3)',
        boxShadow: '0 0 40px rgba(56,189,248,0.1)',
        borderRadius: 24,
        padding: 40,
        width: '100%',
        maxWidth: 800,
        display: 'flex',
        flexDirection: 'column',
        gap: 40
      }}>
        
        {/* Search Bar */}
        <div style={{ display: 'flex', gap: 15 }}>
          <input 
            type="text" 
            placeholder="[ SCAN PATIENT WRISTBAND OR ENTER ID ]"
            style={{
              flex: 1,
              background: 'rgba(0,0,0,0.6)',
              border: '1px solid #00E5FF',
              color: '#FFF',
              padding: 20,
              fontSize: 16,
              letterSpacing: 2,
              outline: 'none',
              boxShadow: 'inset 0 0 15px rgba(0,229,255,0.2)',
              borderRadius: 12
            }}
          />
          <button 
            onClick={() => router.push('/explore')}
            style={{
              background: 'linear-gradient(90deg, #0284C7, #00E5FF)',
              border: 'none',
              color: '#0F172A',
              padding: '0 30px',
              fontSize: 16,
              fontWeight: '900',
              letterSpacing: 2,
              borderRadius: 12,
              cursor: 'pointer',
              boxShadow: '0 0 20px rgba(0,229,255,0.4)',
              transition: 'all 0.3s ease'
            }}
            onMouseOver={(e) => e.currentTarget.style.boxShadow = '0 0 35px rgba(0,229,255,0.7)'}
            onMouseOut={(e) => e.currentTarget.style.boxShadow = '0 0 20px rgba(0,229,255,0.4)'}
          >
            TARGET
          </button>
        </div>

        {/* Recent Patients */}
        <div>
          <h3 style={{ margin: '0 0 20px 0', color: '#94A3B8', fontSize: 14, letterSpacing: 2, textTransform: 'uppercase' }}>Recent Active Patients</h3>
          
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20 }}>
            
            {/* Card 1 */}
            <div 
              onClick={() => router.push('/explore')}
              style={{
                background: 'rgba(30,41,59,0.5)',
                border: '1px solid rgba(56,189,248,0.2)',
                borderRadius: 16,
                padding: 20,
                cursor: 'pointer',
                transition: 'all 0.3s ease',
                boxShadow: '0 4px 15px rgba(0,0,0,0.3)'
              }}
              onMouseOver={(e) => {
                e.currentTarget.style.background = 'rgba(56,189,248,0.1)';
                e.currentTarget.style.border = '1px solid rgba(56,189,248,0.6)';
                e.currentTarget.style.boxShadow = '0 0 20px rgba(56,189,248,0.3)';
              }}
              onMouseOut={(e) => {
                e.currentTarget.style.background = 'rgba(30,41,59,0.5)';
                e.currentTarget.style.border = '1px solid rgba(56,189,248,0.2)';
                e.currentTarget.style.boxShadow = '0 4px 15px rgba(0,0,0,0.3)';
              }}
            >
              <h2 style={{ margin: 0, color: '#FFF', fontSize: 20, fontWeight: 'bold' }}>Anna Chen</h2>
              <div style={{ margin: '8px 0', color: '#38BDF8', fontSize: 12, fontWeight: '900', letterSpacing: 1 }}>ID: VHP-88390</div>
              <div style={{ display: 'inline-block', background: 'rgba(16,185,129,0.2)', border: '1px solid #10B981', color: '#10B981', padding: '4px 10px', borderRadius: 8, fontSize: 11, fontWeight: 'bold' }}>
                Status: Post-Op Day 3
              </div>
            </div>

            {/* Card 2 */}
            <div 
              onClick={() => router.push('/explore')}
              style={{
                background: 'rgba(30,41,59,0.5)',
                border: '1px solid rgba(56,189,248,0.2)',
                borderRadius: 16,
                padding: 20,
                cursor: 'pointer',
                transition: 'all 0.3s ease',
                boxShadow: '0 4px 15px rgba(0,0,0,0.3)'
              }}
              onMouseOver={(e) => {
                e.currentTarget.style.background = 'rgba(56,189,248,0.1)';
                e.currentTarget.style.border = '1px solid rgba(56,189,248,0.6)';
                e.currentTarget.style.boxShadow = '0 0 20px rgba(56,189,248,0.3)';
              }}
              onMouseOut={(e) => {
                e.currentTarget.style.background = 'rgba(30,41,59,0.5)';
                e.currentTarget.style.border = '1px solid rgba(56,189,248,0.2)';
                e.currentTarget.style.boxShadow = '0 4px 15px rgba(0,0,0,0.3)';
              }}
            >
              <h2 style={{ margin: 0, color: '#FFF', fontSize: 20, fontWeight: 'bold' }}>Arjun Sharma</h2>
              <div style={{ margin: '8px 0', color: '#38BDF8', fontSize: 12, fontWeight: '900', letterSpacing: 1 }}>ID: VAAYU-77572</div>
              <div style={{ display: 'inline-block', background: 'rgba(245,158,11,0.2)', border: '1px solid #F59E0B', color: '#F59E0B', padding: '4px 10px', borderRadius: 8, fontSize: 11, fontWeight: 'bold' }}>
                Status: Pre-Op Clearance
              </div>
            </div>

          </div>
        </div>

      </div>
    </div>
  );
}
