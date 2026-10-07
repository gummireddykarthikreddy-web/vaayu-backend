import { Platform } from 'react-native';

if (Platform.OS === 'web' && typeof window !== 'undefined') {
  window.process = window.process || ({} as any);
  window.process.emitWarning = window.process.emitWarning || function () {};
}
