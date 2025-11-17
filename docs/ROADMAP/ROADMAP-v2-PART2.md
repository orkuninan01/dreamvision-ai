# 🗺️ DreamVision AI - Roadmap v2.0 (Continued)

> **This is Part 2 of the roadmap. See ROADMAP-v2.md for Phase 0-2.**

---

## 📋 PHASE 3: Mobile App Development (React Native)

**Timeline:** Week 3-4 (10-12 working days, 60-72 hours)  
**Priority:** P0 (Critical Path)  
**Dependencies:** Phase 2 (Backend)  
**Goal:** Production-ready mobile app with full backend integration

---

### Epic 3.1: Expo Project Setup

**Duration:** Day 1 (5-6 hours)  
**Priority:** P0

#### User Story:
> As a developer, I need a properly configured React Native project so that I can build the mobile app efficiently.

#### Acceptance Criteria:
- [ ] Expo project initialized with TypeScript
- [ ] Project structure organized
- [ ] Navigation configured (React Navigation)
- [ ] State management configured (Zustand)
- [ ] API client configured (Axios + Supabase)
- [ ] Theme system ready
- [ ] Development environment working (iOS & Android)

#### Technical Tasks:

**Task 3.1.1: Project Initialization** (1 hour)
```bash
Priority: P0
Estimated Time: 1 hour

# In dreamvision-ai root:
cd ..  # Go to root
npx create-expo-app@latest mobile --template blank-typescript

cd mobile

# Install core dependencies:
npm install @react-navigation/native @react-navigation/native-stack
npm install @react-navigation/bottom-tabs
npm install react-native-screens react-native-safe-area-context
npm install axios zustand
npm install @supabase/supabase-js
npm install expo-secure-store
npm install expo-av  # For video playback
npm install expo-linking  # For deep linking

# Install UI dependencies:
npm install react-native-paper
# OR
npm install native-base

# Dev dependencies:
npm install --save-dev @types/react @types/react-native
```

**Task 3.1.2: Project Structure** (1 hour)
```bash
Priority: P0
Estimated Time: 1 hour

# Create folder structure:
mkdir -p src/api
mkdir -p src/components/common
mkdir -p src/components/dream
mkdir -p src/screens/auth
mkdir -p src/screens
mkdir -p src/navigation
mkdir -p src/store
mkdir -p src/hooks
mkdir -p src/types
mkdir -p src/utils
mkdir -p src/constants

# Create files:
touch src/api/client.ts
touch src/api/auth.ts
touch src/api/dreams.ts
touch src/api/videos.ts
touch src/constants/theme.ts
touch src/constants/config.ts
touch src/types/index.ts
touch src/utils/storage.ts
touch src/navigation/AppNavigator.tsx
touch src/store/authStore.ts
touch src/store/dreamStore.ts
```

**Task 3.1.3: Environment Configuration** (30 minutes)
```typescript
Priority: P0
Estimated Time: 30 minutes

// Create .env file in mobile/:
EXPO_PUBLIC_API_URL=http://localhost:8000/api/v1
EXPO_PUBLIC_SUPABASE_URL=https://xxxxx.supabase.co
EXPO_PUBLIC_SUPABASE_ANON_KEY=eyJxxx...

// src/constants/config.ts
export const API_URL = process.env.EXPO_PUBLIC_API_URL || 'http://localhost:8000/api/v1';
export const SUPABASE_URL = process.env.EXPO_PUBLIC_SUPABASE_URL || '';
export const SUPABASE_ANON_KEY = process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY || '';

// Update app.json:
{
  "expo": {
    "name": "DreamVision",
    "slug": "dreamvision-ai",
    "version": "1.0.0",
    "orientation": "portrait",
    "icon": "./assets/icon.png",
    "userInterfaceStyle": "dark",
    "splash": {
      "image": "./assets/splash.png",
      "resizeMode": "contain",
      "backgroundColor": "#0F172A"
    },
    "ios": {
      "supportsTablet": true,
      "bundleIdentifier": "com.dreamvision.app"
    },
    "android": {
      "adaptiveIcon": {
        "foregroundImage": "./assets/adaptive-icon.png",
        "backgroundColor": "#0F172A"
      },
      "package": "com.dreamvision.app"
    },
    "plugins": [
      [
        "expo-av",
        {
          "microphonePermission": "Allow DreamVision to access your microphone."
        }
      ]
    ]
  }
}
```

**Task 3.1.4: API Client Setup** (1.5 hours)
```typescript
Priority: P0
Estimated Time: 1.5 hours

// src/api/client.ts
import axios from 'axios';
import { API_URL } from '@/constants/config';
import { getStoredToken } from '@/utils/storage';

const apiClient = axios.create({
  baseURL: API_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor: Add auth token
apiClient.interceptors.request.use(
  async (config) => {
    const token = await getStoredToken();
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor: Handle errors
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      // Token expired, logout user
      // We'll implement this in authStore
    }
    return Promise.reject(error);
  }
);

export default apiClient;

// src/utils/storage.ts
import * as SecureStore from 'expo-secure-store';

const TOKEN_KEY = 'auth_token';
const REFRESH_TOKEN_KEY = 'refresh_token';

export const storeToken = async (token: string): Promise<void> => {
  await SecureStore.setItemAsync(TOKEN_KEY, token);
};

export const getStoredToken = async (): Promise<string | null> => {
  return await SecureStore.getItemAsync(TOKEN_KEY);
};

export const removeToken = async (): Promise<void> => {
  await SecureStore.deleteItemAsync(TOKEN_KEY);
  await SecureStore.deleteItemAsync(REFRESH_TOKEN_KEY);
};

export const storeRefreshToken = async (token: string): Promise<void> => {
  await SecureStore.setItemAsync(REFRESH_TOKEN_KEY, token);
};

export const getRefreshToken = async (): Promise<string | null> => {
  return await SecureStore.getItemAsync(REFRESH_TOKEN_KEY);
};
```

**Task 3.1.5: Theme System** (1 hour)
```typescript
Priority: P0
Estimated Time: 1 hour

// src/constants/theme.ts
export const theme = {
  colors: {
    primary: '#6366F1',      // Indigo
    secondary: '#EC4899',     // Pink
    background: '#0F172A',    // Dark blue
    surface: '#1E293B',       // Lighter dark blue
    card: '#334155',          // Card background
    text: '#F1F5F9',          // Light text
    textSecondary: '#94A3B8', // Secondary text
    border: '#475569',        // Border color
    error: '#EF4444',         // Red
    success: '#10B981',       // Green
    warning: '#F59E0B',       // Yellow
  },
  spacing: {
    xs: 4,
    sm: 8,
    md: 16,
    lg: 24,
    xl: 32,
    xxl: 48,
  },
  borderRadius: {
    sm: 4,
    md: 8,
    lg: 16,
    xl: 24,
    full: 9999,
  },
  fontSize: {
    xs: 12,
    sm: 14,
    md: 16,
    lg: 18,
    xl: 24,
    xxl: 32,
  },
  fontWeight: {
    regular: '400',
    medium: '500',
    semibold: '600',
    bold: '700',
  },
};

export type Theme = typeof theme;
```

**Task 3.1.6: TypeScript Types** (30 minutes)
```typescript
Priority: P0
Estimated Time: 30 minutes

// src/types/index.ts
export interface User {
  id: string;
  email: string;
  username: string;
  subscription_tier: 'free' | 'premium';
  dreams_count: number;
  videos_count: number;
  created_at: string;
}

export interface Dream {
  id: string;
  user_id: string;
  dream_text: string;
  video_prompt: string;
  category: string;
  template_used: string;
  confidence: number;
  created_at: string;
  video?: Video;
}

export interface Video {
  id: string;
  dream_id: string;
  job_id: string;
  status: 'pending' | 'processing' | 'completed' | 'failed';
  video_url?: string;
  thumbnail_url?: string;
  duration: number;
  created_at: string;
  completed_at?: string;
  progress?: number;
}

export interface DreamAnalysisResponse {
  dream_id: string;
  video_prompt: string;
  category: string;
  template_used: string;
  confidence: number;
  token_usage: {
    input: number;
    output: number;
  };
  processing_time_ms: number;
  created_at: string;
}

export interface CombinedDreamVideoResponse {
  dream_analysis: DreamAnalysisResponse;
  video_generation: {
    video_id: string;
    job_id: string;
    status: string;
    created_at: string;
    estimated_completion_time: string;
  };
}
```

#### Deliverables:
- [ ] Expo project initialized
- [ ] Project structure organized
- [ ] API client configured
- [ ] Environment variables set
- [ ] Theme system ready
- [ ] TypeScript types defined
- [ ] App runs on iOS/Android

#### Testing Checklist:
```bash
# Start Expo:
cd mobile
npx expo start

# Test on device:
- [ ] Scan QR with Expo Go (iOS/Android)
- [ ] App launches without errors
- [ ] See blank screen (expected, no UI yet)

# Test API connection:
- [ ] API_URL points to your backend
- [ ] No CORS errors in console
```

---

### Epic 3.2: State Management & API Integration

**Duration:** Day 2 (5-6 hours)  
**Priority:** P0  
**Dependencies:** Epic 3.1

#### User Story:
> As a developer, I need state management and API services so that the app can communicate with the backend.

#### Acceptance Criteria:
- [ ] Auth store manages authentication state
- [ ] Dream store manages dream/video state
- [ ] API services for auth, dreams, videos
- [ ] Token persistence working
- [ ] Error handling in place

#### Technical Tasks:

**Task 3.2.1: Auth Store** (2 hours)
```typescript
Priority: P0
Estimated Time: 2 hours

// src/store/authStore.ts
import { create } from 'zustand';
import { User } from '@/types';
import { storeToken, getStoredToken, removeToken } from '@/utils/storage';
import * as authApi from '@/api/auth';

interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;
  
  // Actions
  register: (email: string, password: string, username: string) => Promise<void>;
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  loadUser: () => Promise<void>;
  clearError: () => void;
}

export const useAuthStore = create<AuthState>((set, get) => ({
  user: null,
  token: null,
  isAuthenticated: false,
  isLoading: false,
  error: null,
  
  register: async (email, password, username) => {
    set({ isLoading: true, error: null });
    try {
      const response = await authApi.register(email, password, username);
      await storeToken(response.access_token);
      set({
        user: response.user,
        token: response.access_token,
        isAuthenticated: true,
        isLoading: false,
      });
    } catch (error: any) {
      set({
        error: error.response?.data?.detail || 'Registration failed',
        isLoading: false,
      });
      throw error;
    }
  },
  
  login: async (email, password) => {
    set({ isLoading: true, error: null });
    try {
      const response = await authApi.login(email, password);
      await storeToken(response.access_token);
      set({
        user: response.user,
        token: response.access_token,
        isAuthenticated: true,
        isLoading: false,
      });
    } catch (error: any) {
      set({
        error: error.response?.data?.detail || 'Login failed',
        isLoading: false,
      });
      throw error;
    }
  },
  
  logout: async () => {
    await removeToken();
    set({
      user: null,
      token: null,
      isAuthenticated: false,
      error: null,
    });
  },
  
  loadUser: async () => {
    const token = await getStoredToken();
    if (!token) {
      set({ isAuthenticated: false });
      return;
    }
    
    try {
      const user = await authApi.getCurrentUser();
      set({
        user,
        token,
        isAuthenticated: true,
      });
    } catch (error) {
      await removeToken();
      set({
        user: null,
        token: null,
        isAuthenticated: false,
      });
    }
  },
  
  clearError: () => set({ error: null }),
}));
```

**Task 3.2.2: Dream Store** (2 hours)
```typescript
Priority: P0
Estimated Time: 2 hours

// src/store/dreamStore.ts
import { create } from 'zustand';
import { Dream, Video, CombinedDreamVideoResponse } from '@/types';
import * as dreamsApi from '@/api/dreams';
import * as videosApi from '@/api/videos';

interface DreamState {
  dreams: Dream[];
  currentDream: Dream | null;
  currentVideo: Video | null;
  isLoading: boolean;
  isGenerating: boolean;
  error: string | null;
  
  // Pagination
  page: number;
  totalPages: number;
  hasMore: boolean;
  
  // Actions
  generateDreamVideo: (dreamText: string) => Promise<CombinedDreamVideoResponse>;
  pollVideoStatus: (jobId: string) => Promise<Video>;
  fetchDreams: (page?: number, category?: string) => Promise<void>;
  fetchDreamById: (dreamId: string) => Promise<void>;
  clearError: () => void;
  reset: () => void;
}

export const useDreamStore = create<DreamState>((set, get) => ({
  dreams: [],
  currentDream: null,
  currentVideo: null,
  isLoading: false,
  isGenerating: false,
  error: null,
  page: 1,
  totalPages: 1,
  hasMore: true,
  
  generateDreamVideo: async (dreamText) => {
    set({ isGenerating: true, error: null });
    try {
      const response = await dreamsApi.generateDreamVideo(dreamText);
      set({
        currentDream: {
          id: response.dream_analysis.dream_id,
          dream_text: dreamText,
          video_prompt: response.dream_analysis.video_prompt,
          category: response.dream_analysis.category,
          template_used: response.dream_analysis.template_used,
          confidence: response.dream_analysis.confidence,
          created_at: response.dream_analysis.created_at,
          user_id: '', // Will be filled from backend
        } as Dream,
        currentVideo: {
          id: response.video_generation.video_id,
          job_id: response.video_generation.job_id,
          status: response.video_generation.status,
          duration: 5,
          created_at: response.video_generation.created_at,
        } as Video,
        isGenerating: false,
      });
      return response;
    } catch (error: any) {
      set({
        error: error.response?.data?.detail || 'Failed to generate dream video',
        isGenerating: false,
      });
      throw error;
    }
  },
  
  pollVideoStatus: async (jobId) => {
    try {
      const video = await videosApi.getVideoStatus(jobId);
      set({ currentVideo: video });
      return video;
    } catch (error: any) {
      set({
        error: error.response?.data?.detail || 'Failed to get video status',
      });
      throw error;
    }
  },
  
  fetchDreams: async (page = 1, category) => {
    set({ isLoading: true, error: null });
    try {
      const response = await dreamsApi.getDreams(page, 20, category);
      set({
        dreams: page === 1 ? response.dreams : [...get().dreams, ...response.dreams],
        page: response.page,
        totalPages: response.pages,
        hasMore: response.page < response.pages,
        isLoading: false,
      });
    } catch (error: any) {
      set({
        error: error.response?.data?.detail || 'Failed to fetch dreams',
        isLoading: false,
      });
      throw error;
    }
  },
  
  fetchDreamById: async (dreamId) => {
    set({ isLoading: true, error: null });
    try {
      const dream = await dreamsApi.getDreamById(dreamId);
      set({
        currentDream: dream,
        currentVideo: dream.video || null,
        isLoading: false,
      });
    } catch (error: any) {
      set({
        error: error.response?.data?.detail || 'Failed to fetch dream',
        isLoading: false,
      });
      throw error;
    }
  },
  
  clearError: () => set({ error: null }),
  
  reset: () => set({
    dreams: [],
    currentDream: null,
    currentVideo: null,
    page: 1,
    totalPages: 1,
    hasMore: true,
    error: null,
  }),
}));
```

**Task 3.2.3: API Services** (1.5 hours)
```typescript
Priority: P0
Estimated Time: 1.5 hours

// src/api/auth.ts
import apiClient from './client';
import { User } from '@/types';

interface RegisterResponse {
  access_token: string;
  refresh_token: string;
  user: User;
}

export const register = async (
  email: string,
  password: string,
  username: string
): Promise<RegisterResponse> => {
  const response = await apiClient.post('/auth/register', {
    email,
    password,
    username,
  });
  return response.data;
};

export const login = async (
  email: string,
  password: string
): Promise<RegisterResponse> => {
  const response = await apiClient.post('/auth/login', {
    email,
    password,
  });
  return response.data;
};

export const getCurrentUser = async (): Promise<User> => {
  const response = await apiClient.get('/auth/me');
  return response.data;
};

// src/api/dreams.ts
import apiClient from './client';
import { Dream, CombinedDreamVideoResponse } from '@/types';

export const generateDreamVideo = async (
  dreamText: string
): Promise<CombinedDreamVideoResponse> => {
  const response = await apiClient.post('/dreams/generate-video', {
    dream_text: dreamText,
    duration: 5,
  });
  return response.data;
};

export const getDreams = async (
  page: number = 1,
  limit: number = 20,
  category?: string
): Promise<{ dreams: Dream[]; total: number; page: number; pages: number }> => {
  const params = { page, limit, ...(category && { category }) };
  const response = await apiClient.get('/dreams', { params });
  return response.data;
};

export const getDreamById = async (dreamId: string): Promise<Dream> => {
  const response = await apiClient.get(`/dreams/${dreamId}`);
  return response.data;
};

// src/api/videos.ts
import apiClient from './client';
import { Video } from '@/types';

export const getVideoStatus = async (jobId: string): Promise<Video> => {
  const response = await apiClient.get(`/videos/${jobId}`);
  return response.data;
};
```

#### Deliverables:
- [ ] Auth store working
- [ ] Dream store working
- [ ] API services implemented
- [ ] Token persistence working
- [ ] Error handling in place

---

### Epic 3.3: Authentication Screens

**Duration:** Day 3 (5-6 hours)  
**Priority:** P0  
**Dependencies:** Epic 3.2

#### User Story:
> As a user, I want to register and login so that I can use the app.

#### Acceptance Criteria:
- [ ] Welcome screen with branding
- [ ] Register screen with validation
- [ ] Login screen
- [ ] Form validation working
- [ ] Loading states shown
- [ ] Error messages displayed
- [ ] Navigation to home after login

#### Technical Tasks:

**Task 3.3.1: Common Components** (1.5 hours)
```typescript
Priority: P0
Estimated Time: 1.5 hours

// src/components/common/Button.tsx
import React from 'react';
import { TouchableOpacity, Text, StyleSheet, ActivityIndicator } from 'react-native';
import { theme } from '@/constants/theme';

interface ButtonProps {
  title: string;
  onPress: () => void;
  variant?: 'primary' | 'secondary' | 'outline';
  loading?: boolean;
  disabled?: boolean;
}

export const Button: React.FC<ButtonProps> = ({
  title,
  onPress,
  variant = 'primary',
  loading = false,
  disabled = false,
}) => {
  return (
    <TouchableOpacity
      style={[
        styles.button,
        variant === 'primary' && styles.primaryButton,
        variant === 'secondary' && styles.secondaryButton,
        variant === 'outline' && styles.outlineButton,
        (disabled || loading) && styles.disabledButton,
      ]}
      onPress={onPress}
      disabled={disabled || loading}
    >
      {loading ? (
        <ActivityIndicator color={theme.colors.text} />
      ) : (
        <Text
          style={[
            styles.buttonText,
            variant === 'outline' && styles.outlineButtonText,
          ]}
        >
          {title}
        </Text>
      )}
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  button: {
    paddingVertical: 16,
    paddingHorizontal: 32,
    borderRadius: theme.borderRadius.md,
    alignItems: 'center',
    justifyContent: 'center',
  },
  primaryButton: {
    backgroundColor: theme.colors.primary,
  },
  secondaryButton: {
    backgroundColor: theme.colors.secondary,
  },
  outlineButton: {
    backgroundColor: 'transparent',
    borderWidth: 2,
    borderColor: theme.colors.primary,
  },
  disabledButton: {
    opacity: 0.5,
  },
  buttonText: {
    color: theme.colors.text,
    fontSize: theme.fontSize.md,
    fontWeight: theme.fontWeight.semibold,
  },
  outlineButtonText: {
    color: theme.colors.primary,
  },
});

// src/components/common/Input.tsx
import React, { useState } from 'react';
import {
  View,
  TextInput,
  Text,
  StyleSheet,
  TouchableOpacity,
} from 'react-native';
import { theme } from '@/constants/theme';
import { Ionicons } from '@expo/vector-icons';

interface InputProps {
  label: string;
  value: string;
  onChangeText: (text: string) => void;
  placeholder?: string;
  secureTextEntry?: boolean;
  error?: string;
  keyboardType?: 'default' | 'email-address' | 'numeric';
  autoCapitalize?: 'none' | 'sentences' | 'words' | 'characters';
}

export const Input: React.FC<InputProps> = ({
  label,
  value,
  onChangeText,
  placeholder,
  secureTextEntry = false,
  error,
  keyboardType = 'default',
  autoCapitalize = 'none',
}) => {
  const [showPassword, setShowPassword] = useState(false);
  
  return (
    <View style={styles.container}>
      <Text style={styles.label}>{label}</Text>
      <View style={styles.inputContainer}>
        <TextInput
          style={[styles.input, error && styles.inputError]}
          value={value}
          onChangeText={onChangeText}
          placeholder={placeholder}
          placeholderTextColor={theme.colors.textSecondary}
          secureTextEntry={secureTextEntry && !showPassword}
          keyboardType={keyboardType}
          autoCapitalize={autoCapitalize}
        />
        {secureTextEntry && (
          <TouchableOpacity
            style={styles.eyeIcon}
            onPress={() => setShowPassword(!showPassword)}
          >
            <Ionicons
              name={showPassword ? 'eye-off' : 'eye'}
              size={24}
              color={theme.colors.textSecondary}
            />
          </TouchableOpacity>
        )}
      </View>
      {error && <Text style={styles.error}>{error}</Text>}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginBottom: theme.spacing.md,
  },
  label: {
    color: theme.colors.text,
    fontSize: theme.fontSize.sm,
    fontWeight: theme.fontWeight.medium,
    marginBottom: theme.spacing.xs,
  },
  inputContainer: {
    position: 'relative',
  },
  input: {
    backgroundColor: theme.colors.surface,
    color: theme.colors.text,
    padding: theme.spacing.md,
    borderRadius: theme.borderRadius.md,
    fontSize: theme.fontSize.md,
    borderWidth: 1,
    borderColor: 'transparent',
  },
  inputError: {
    borderColor: theme.colors.error,
  },
  eyeIcon: {
    position: 'absolute',
    right: theme.spacing.md,
    top: '50%',
    transform: [{ translateY: -12 }],
  },
  error: {
    color: theme.colors.error,
    fontSize: theme.fontSize.xs,
    marginTop: theme.spacing.xs,
  },
});
```

**Task 3.3.2: Welcome Screen** (1 hour)
```typescript
Priority: P0
Estimated Time: 1 hour

// src/screens/auth/WelcomeScreen.tsx
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { Button } from '@/components/common/Button';
import { theme } from '@/constants/theme';

export const WelcomeScreen: React.FC<{ navigation: any }> = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.emoji}>🌙</Text>
        <Text style={styles.title}>DreamVision AI</Text>
        <Text style={styles.subtitle}>
          Turn your dreams into cinematic videos
        </Text>
      </View>
      
      <View style={styles.buttons}>
        <Button
          title="Get Started"
          onPress={() => navigation.navigate('Register')}
        />
        <TouchableOpacity
          onPress={() => navigation.navigate('Login')}
          style={styles.loginLink}
        >
          <Text style={styles.loginText}>
            Already have an account? <Text style={styles.loginTextBold}>Sign In</Text>
          </Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: theme.colors.background,
    padding: theme.spacing.xl,
    justifyContent: 'space-between',
  },
  content: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  emoji: {
    fontSize: 80,
    marginBottom: theme.spacing.lg,
  },
  title: {
    fontSize: theme.fontSize.xxl,
    fontWeight: theme.fontWeight.bold,
    color: theme.colors.text,
    marginBottom: theme.spacing.sm,
  },
  subtitle: {
    fontSize: theme.fontSize.md,
    color: theme.colors.textSecondary,
    textAlign: 'center',
  },
  buttons: {
    gap: theme.spacing.md,
  },
  loginLink: {
    alignItems: 'center',
    paddingVertical: theme.spacing.md,
  },
  loginText: {
    color: theme.colors.textSecondary,
    fontSize: theme.fontSize.sm,
  },
  loginTextBold: {
    color: theme.colors.primary,
    fontWeight: theme.fontWeight.semibold,
  },
});
```

**Task 3.3.3: Register Screen** (1.5 hours)
```typescript
Priority: P0
Estimated Time: 1.5 hours

// src/screens/auth/RegisterScreen.tsx
import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Alert,
} from 'react-native';
import { Input } from '@/components/common/Input';
import { Button } from '@/components/common/Button';
import { useAuthStore } from '@/store/authStore';
import { theme } from '@/constants/theme';

export const RegisterScreen: React.FC<{ navigation: any }> = ({ navigation }) => {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [errors, setErrors] = useState<Record<string, string>>({});
  
  const { register, isLoading, error: authError } = useAuthStore();
  
  const validateForm = () => {
    const newErrors: Record<string, string> = {};
    
    if (!email) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      newErrors.email = 'Email is invalid';
    }
    
    if (!username) {
      newErrors.username = 'Username is required';
    } else if (username.length < 3) {
      newErrors.username = 'Username must be at least 3 characters';
    }
    
    if (!password) {
      newErrors.password = 'Password is required';
    } else if (password.length < 8) {
      newErrors.password = 'Password must be at least 8 characters';
    } else if (!/[A-Z]/.test(password)) {
      newErrors.password = 'Password must contain an uppercase letter';
    } else if (!/[0-9]/.test(password)) {
      newErrors.password = 'Password must contain a number';
    }
    
    if (password !== confirmPassword) {
      newErrors.confirmPassword = 'Passwords do not match';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };
  
  const handleRegister = async () => {
    if (!validateForm()) return;
    
    try {
      await register(email, password, username);
      navigation.replace('Main');
    } catch (error) {
      Alert.alert('Registration Failed', authError || 'Please try again');
    }
  };
  
  return (
    <ScrollView style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.title}>Create Account</Text>
        <Text style={styles.subtitle}>
          Start turning your dreams into videos
        </Text>
        
        <View style={styles.form}>
          <Input
            label="Email"
            value={email}
            onChangeText={setEmail}
            placeholder="your@email.com"
            keyboardType="email-address"
            error={errors.email}
          />
          
          <Input
            label="Username"
            value={username}
            onChangeText={setUsername}
            placeholder="dreamuser"
            error={errors.username}
          />
          
          <Input
            label="Password"
            value={password}
            onChangeText={setPassword}
            placeholder="••••••••"
            secureTextEntry
            error={errors.password}
          />
          
          <Input
            label="Confirm Password"
            value={confirmPassword}
            onChangeText={setConfirmPassword}
            placeholder="••••••••"
            secureTextEntry
            error={errors.confirmPassword}
          />
          
          <Button
            title="Sign Up"
            onPress={handleRegister}
            loading={isLoading}
          />
          
          <TouchableOpacity
            onPress={() => navigation.navigate('Login')}
            style={styles.linkContainer}
          >
            <Text style={styles.linkText}>
              Already have an account? <Text style={styles.linkTextBold}>Sign In</Text>
            </Text>
          </TouchableOpacity>
        </View>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: theme.colors.background,
  },
  content: {
    padding: theme.spacing.xl,
  },
  title: {
    fontSize: theme.fontSize.xxl,
    fontWeight: theme.fontWeight.bold,
    color: theme.colors.text,
    marginBottom: theme.spacing.sm,
  },
  subtitle: {
    fontSize: theme.fontSize.md,
    color: theme.colors.textSecondary,
    marginBottom: theme.spacing.xl,
  },
  form: {
    gap: theme.spacing.md,
  },
  linkContainer: {
    alignItems: 'center',
    paddingVertical: theme.spacing.md,
  },
  linkText: {
    color: theme.colors.textSecondary,
    fontSize: theme.fontSize.sm,
  },
  linkTextBold: {
    color: theme.colors.primary,
    fontWeight: theme.fontWeight.semibold,
  },
});
```

**Task 3.3.4: Login Screen** (1 hour)
```typescript
Priority: P0
Estimated Time: 1 hour

// src/screens/auth/LoginScreen.tsx
import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Alert,
} from 'react-native';
import { Input } from '@/components/common/Input';
import { Button } from '@/components/common/Button';
import { useAuthStore } from '@/store/authStore';
import { theme } from '@/constants/theme';

export const LoginScreen: React.FC<{ navigation: any }> = ({ navigation }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState<Record<string, string>>({});
  
  const { login, isLoading, error: authError } = useAuthStore();
  
  const validateForm = () => {
    const newErrors: Record<string, string> = {};
    
    if (!email) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      newErrors.email = 'Email is invalid';
    }
    
    if (!password) {
      newErrors.password = 'Password is required';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };
  
  const handleLogin = async () => {
    if (!validateForm()) return;
    
    try {
      await login(email, password);
      navigation.replace('Main');
    } catch (error) {
      Alert.alert('Login Failed', authError || 'Invalid email or password');
    }
  };
  
  return (
    <ScrollView style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.title}>Welcome Back</Text>
        <Text style={styles.subtitle}>
          Sign in to continue creating dream videos
        </Text>
        
        <View style={styles.form}>
          <Input
            label="Email"
            value={email}
            onChangeText={setEmail}
            placeholder="your@email.com"
            keyboardType="email-address"
            error={errors.email}
          />
          
          <Input
            label="Password"
            value={password}
            onChangeText={setPassword}
            placeholder="••••••••"
            secureTextEntry
            error={errors.password}
          />
          
          <Button
            title="Sign In"
            onPress={handleLogin}
            loading={isLoading}
          />
          
          <TouchableOpacity
            onPress={() => navigation.navigate('Register')}
            style={styles.linkContainer}
          >
            <Text style={styles.linkText}>
              Don't have an account? <Text style={styles.linkTextBold}>Sign Up</Text>
            </Text>
          </TouchableOpacity>
        </View>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  // Same styles as RegisterScreen
  ...RegisterScreen.styles,
});
```

#### Deliverables:
- [ ] Welcome screen
- [ ] Register screen with validation
- [ ] Login screen
- [ ] Common UI components (Button, Input)
- [ ] Form validation working
- [ ] Navigation after auth

---

**Due to length limits, Phase 3-7 continues in next message...**

**What's Ready So Far:**
- ✅ Phase 2: Complete backend (Supabase + FastAPI + AI integration)
- ✅ Phase 3: Started (Project setup, state management, auth screens)

**Next:** I'll continue with:
- Phase 3 (rest): Main app screens (Dream input, Video player, History)
- Phase 4: Integration & polish
- Phase 5: Testing & deployment
- Phase 6-7: Optional features (Web PWA, Analytics)

Devam edeyim mi? 🚀
