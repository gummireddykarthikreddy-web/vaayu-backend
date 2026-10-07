const { getDefaultConfig } = require('expo/metro-config');

const config = getDefaultConfig(__dirname);

// Add support for .mjs and .cjs (needed for @react-three/fiber and three)
config.resolver.sourceExts.push('mjs', 'cjs');

// Ensure Metro resolves package exports correctly (fixes the InvalidPackageError for r3f)
config.resolver.unstable_enablePackageExports = true;
config.resolver.unstable_conditionNames = ['browser', 'require', 'react-native'];

module.exports = config;
