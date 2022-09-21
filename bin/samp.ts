#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { SampStack } from '../lib/samp-stack';

const app = new cdk.App();
new SampStack(app, 'SampStack');
