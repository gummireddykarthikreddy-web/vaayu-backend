import axios from 'axios';
import { useState } from 'react';
import {
    ActivityIndicator,
    ScrollView,
    StyleSheet,
    Text,
    TextInput,
    TouchableOpacity,
    View
} from 'react-native';
import { API_BASE_URL } from '../constants/api';

export default function DoctorVault() {
  const [searchId, setSearchId] = useState('');
  const [patientData, setPatientData] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const fetchPatientData = async () => {
    if (!searchId.trim()) return;
    
    setLoading(true);
    setError('');
    setPatientData(null);

    try {
      const response = await axios.get(`${API_BASE_URL}/api/patient/${searchId}`);
      
      if (response.data.status === 'success') {
        setPatientData(response.data);
      } else {
        setError(response.data.message || 'Patient not found.');
      }
    } catch (err) {
      setError('Could not connect to the server. Is the backend running?');
    } finally {
      setLoading(false);
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Vaayu Clinical Portal</Text>
        <Text style={styles.subtitle}>Enter a Patient ID to securely access their Medical Vault.</Text>
      </View>

      <View style={styles.searchCard}>
        <TextInput
          style={styles.input}
          placeholder="e.g., VAAYU-8ABF3DB9"
          value={searchId}
          onChangeText={setSearchId}
          autoCapitalize="characters"
        />
        <TouchableOpacity style={styles.searchButton} onPress={fetchPatientData}>
          <Text style={styles.buttonText}>Access Records</Text>
        </TouchableOpacity>
      </View>

      {error ? <Text style={styles.errorText}>{error}</Text> : null}
      {loading ? <ActivityIndicator size="large" color="#2980B9" style={{ marginTop: 30 }} /> : null}

      {patientData && !loading && (
        <View style={styles.vaultCard}>
          <View style={styles.profileHeader}>
            <Text style={styles.patientName}>{patientData.patient_info?.name || patientData.profile?.name}</Text>
            <View style={styles.badgeRow}>
              <Text style={styles.badge}>Blood: {patientData.patient_info?.blood_group || patientData.profile?.blood_group}</Text>
            </View>
          </View>
          <View style={styles.section}>
             <Text style={styles.sectionTitle}>Please use Explore tab for full features.</Text>
          </View>
        </View>
      )}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flexGrow: 1, backgroundColor: '#ECF0F1', padding: 20 },
  header: { marginBottom: 25, marginTop: 20 },
  title: { fontSize: 26, fontWeight: 'bold', color: '#2C3E50' },
  subtitle: { fontSize: 14, color: '#7F8C8D', marginTop: 5 },
  searchCard: { backgroundColor: '#FFFFFF', padding: 15, borderRadius: 12, elevation: 2, marginBottom: 20 },
  input: { borderWidth: 1, borderColor: '#BDC3C7', borderRadius: 8, padding: 12, fontSize: 16, backgroundColor: '#F8FAFC', marginBottom: 15 },
  searchButton: { backgroundColor: '#2980B9', padding: 15, borderRadius: 8, alignItems: 'center' },
  buttonText: { color: '#FFFFFF', fontSize: 16, fontWeight: 'bold' },
  errorText: { color: '#E74C3C', textAlign: 'center', marginBottom: 20, fontWeight: '600' },
  vaultCard: { backgroundColor: '#FFFFFF', borderRadius: 12, padding: 20, elevation: 2 },
  profileHeader: { borderBottomWidth: 1, borderBottomColor: '#ECF0F1', paddingBottom: 15, marginBottom: 15 },
  patientName: { fontSize: 22, fontWeight: 'bold', color: '#2C3E50' },
  badgeRow: { flexDirection: 'row', marginTop: 10, gap: 10 },
  badge: { backgroundColor: '#E8F8F5', color: '#16A085', paddingHorizontal: 12, paddingVertical: 5, borderRadius: 15, fontWeight: '600', overflow: 'hidden' },
  section: { marginBottom: 20 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', color: '#34495E', marginBottom: 10 },
});